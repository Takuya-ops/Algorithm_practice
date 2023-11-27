def minRewards(scores):
    rewards = [1 for _ in scores]

    for i in range(len(scores) - 1):
        if scores[i] < scores[i + 1]:
            rewards[i + 1] = rewards[i] + 1

    for i in reversed(range(1, len(scores))):
        if scores[i - 1] > scores[i]:
            rewards[i - 1] = max(rewards[i] + 1, rewards[i - 1])

    return rewards, sum(rewards)


if __name__ == "__main__":
    # テスト用の点数
    sample_scores1 = [4, 2, 5, 3, 4]
    sample_scores2 = [8, 4, 2, 1, 3, 6]

    print("Sample Scores 1:", sample_scores1)
    rewards1, total_rewards1 = minRewards(sample_scores1)
    print("Total Rewards 1:", rewards1)
    print("Total Rewards 1:", total_rewards1)

    print("Sample Scores 2:", sample_scores2)
    rewards2, total_rewards2 = minRewards(sample_scores2)
    print("Total Rewards 2:", rewards2)
    print("Total Rewards 2:", total_rewards2)
