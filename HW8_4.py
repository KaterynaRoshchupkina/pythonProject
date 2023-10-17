result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
repeat_count = {}
for repeat in result_link:
    repeat_count[repeat] = repeat_count.get(repeat, 0) + 1
print(repeat_count)
