N = int(input())
for i in range(1, N + 1):
    tmp_str = str(i)
    clap_count = tmp_str.count("3") + tmp_str.count("6") + tmp_str.count("9")
    if clap_count == 1:
        print("-", end=" ")
    elif clap_count > 1:
        print("-" * clap_count, end=" ")
    elif clap_count == 0:
        print(tmp_str, end=" ")