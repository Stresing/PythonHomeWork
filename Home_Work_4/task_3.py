''' Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.'''
count: int = 1


def save_operation(**kwargs):  # Записывает операции поступления и списания которые происходят в задаче 1, лекции 2
    global count
    with open("Operation.txt", 'a+', encoding="utf-8") as file:

        for key, values in kwargs.items():
            if key == "replenish":
                file.write(f"Операция {count}: Поступление в размере {values}\n")
                count += 1
            elif key == "withdrawals":
                file.write(f"Операция {count}: Списание в размере {values}\n")
                count += 1
