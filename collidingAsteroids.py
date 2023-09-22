def collidingAsteroids(asteroids):
    stack = []

    for asteroid in asteroids:
        if not stack or asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)

    return stack


# テスト用例
asteroids = [5, 10, -5]
result = collidingAsteroids(asteroids)
print(result)  # 出力: [5, 10]
