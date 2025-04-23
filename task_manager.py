tasks = []

def add_task(task_list, datetime, title):
    new_task = {"datetime": datetime, "title": title}
    task_list.append(new_task)

def show_tasks(task_list):
    print("登録されたタスク一覧：")
    for i, t in enumerate(task_list):
        print(f"{i}: {t['datetime']} - {t['title']}")

def delete_task(task_list):
    show_tasks(task_list)
    index = input("削除したいタスクの番号を入力してください")
    if index.isdigit():
        index = int(index)
        if 0<= index < len(task_list):
            deleted = task_list.pop(index)
            print(f"削除しました：{deleted['datetime']} - {deleted['title']}")
        else:
            print("無効な数字です")
    else:
        print("数字を入力してください")

while True:
    add_task(tasks, input("日付を入力してください"), input("予定を入力してください"))

    again = input("もう１件入力しますか?(y/n)")
    if again.lower() != "y":
        break

print("登録されたタスク一覧:")
for task in tasks:
    print(f"・{task['datetime']} - {task['title']}")

delete =input("削除したいタスクはありますか？(y/n)")
if delete.lower() == "y":
    delete_task(tasks)

print("現在のタスクリスト：")
show_tasks(tasks)