from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    n = data['n']
    start = tuple(data['start'])
    end = tuple(data['end'])
    obstacles = [tuple(obs) for obs in data['obstacles']]

    # 定義動作：0: 上, 1: 右, 2: 下, 3: 左
    actions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    action_symbols = ['↑', '→', '↓', '←']

    # 初始化價值矩陣
    V = {(r, c): 0.0 for r in range(n) for c in range(n)}
    gamma = 0.9      # 折扣因子
    theta = 1e-4     # 收斂門檻
    reward_step = -1 # 每走一步的懲罰

    # 1. 價值迭代 (Value Iteration) - 找出每個狀態的最佳價值
    while True:
        delta = 0
        new_V = V.copy()
        for r in range(n):
            for c in range(n):
                state = (r, c)
                # 終點和障礙物不計算價值
                if state == end or state in obstacles:
                    continue

                # 嘗試 4 個動作，找出能帶來最大價值的動作
                max_value = float('-inf')
                for a in range(4):
                    dr, dc = actions[a]
                    next_r, next_c = r + dr, c + dc

                    # 檢查邊界與障礙物（撞牆則留在原地）
                    if (next_r < 0 or next_r >= n or 
                        next_c < 0 or next_c >= n or 
                        (next_r, next_c) in obstacles):
                        next_state = state
                    else:
                        next_state = (next_r, next_c)

                    # 計算該動作的價值 Q(s, a)
                    q_value = reward_step + gamma * V[next_state]
                    if q_value > max_value:
                        max_value = q_value

                # 更新為最大價值
                new_V[state] = max_value
                delta = max(delta, abs(V[state] - new_V[state]))

        V = new_V
        if delta < theta:
            break

    # 2. 提取最佳策略 (Extract Optimal Policy) - 根據算好的價值決定箭頭方向
    policy = {}
    for r in range(n):
        for c in range(n):
            state = (r, c)
            if state == end or state in obstacles:
                continue

            best_action = 0
            max_value = float('-inf')
            
            for a in range(4):
                dr, dc = actions[a]
                next_r, next_c = r + dr, c + dc

                if (next_r < 0 or next_r >= n or 
                    next_c < 0 or next_c >= n or 
                    (next_r, next_c) in obstacles):
                    next_state = state
                else:
                    next_state = (next_r, next_c)

                q_value = reward_step + gamma * V[next_state]
                if q_value > max_value:
                    max_value = q_value
                    best_action = a
            
            policy[state] = best_action

    # 3. 格式化輸出資料供前端顯示
    formatted_policy = []
    formatted_values = []
    for r in range(n):
        pol_row = []
        val_row = []
        for c in range(n):
            state = (r, c)
            if state == end:
                pol_row.append('🏁')
                val_row.append(0.0)
            elif state in obstacles:
                pol_row.append('X')
                val_row.append('X')
            else:
                pol_row.append(action_symbols[policy[state]])
                val_row.append(round(V[state], 2))
        formatted_policy.append(pol_row)
        formatted_values.append(val_row)

    return jsonify({
        'policy': formatted_policy,
        'values': formatted_values
    })

if __name__ == '__main__':
    app.run(debug=True)