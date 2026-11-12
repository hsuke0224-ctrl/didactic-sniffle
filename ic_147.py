def menu():
  #ここに処理の中身を書く()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。 消す

  functions =["乗車駅選択", "チャージ機能"]

  print("【ウチダ電鉄 交通系 IC カード検証システム】")
  
  for i in range(len(functions)):
    print(i+1,":",functions[i])

  n=int(input("使用する機能を入力してください（終了する場合には99 を入力）"))
  return n

  
  

def select_station():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def pay():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def charge():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def main():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。
  menu() 
  if menu == 1:
    print("乗車駅選択をえらんだ")
  else:
    print("2を選んだ")

if __name__ == "__main__":
    main() 
