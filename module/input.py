def InputProcesser(number_of_choices, check = False):
    range_flag = False
    check_flag = False
    while True:
        inline = input()
        if inline <= number_of_choices:
            range_flag = True
        else:
            print("この値は対応していません")
            continue

        if check == False:
            check_flag = True
        else:
            print(str(inline)+"本当によろしいですか?(y/n)")
            ans = input()
            if ans in ["y", "Y", "yes", "YES"]:
                check_flag = True
            elif ans in ["n", "N", "no", "NO"]:
                continue
            else:
                print("この値は対応していません")
                continue
        if range_flag and check_flag:
            break
    return inline