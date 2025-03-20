def longest_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)] # Инициализирую пустую таблицу
    max_length = 0 # максимальная длина последовательности
    end_index = 0 # индекс окончания самой длинной последовательности
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0
    print(dp)
    result = s1[end_index-max_length:end_index]
    return result


if __name__ == "__main__":
    s1 = "abcdef"
    s2 = "zbcdf"
    print(longest_substring(s1, s2))  # Вывод: "bcd"

