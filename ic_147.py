def menu():
  #ここに処理の中身を書く()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。
  functions =["乗車駅選択", "チャージ機能"]

  print("【ウチダ電鉄 交通系 IC カード検証システム】")
  
  for i in range(len(functions)):
    print(i+1,":",functions[i])

  n=int(input("使用する機能を入力してください（終了する場合には99 を入力）"))
  return n

  
  

def select_station():
  stations=["秋葉原駅","山梨駅","長野駅"]
  fares=[133,4128,7990]
  i=len(stations)
  print("【乗車駅選択】")
  for x in range(i):
    print(x,":",stations[x],"から",fares[x],"円")
  destination = int(input("乗車した駅を入力してください(キャンセルする場合には 99 を入力)"))

  n=destination-1
  while True:
    if destination==1:
      print("乗車駅は",stations[n],"で運賃は ",fares[n]," 円です。")
      return fares[n]
    elif destination==2:
      print("乗車駅は",stations[n],"で運賃は",fares[n],"円です。")
      return fares[n]
    elif destination==3:
      print("乗車駅は",stations[n],"で運賃は",fares[n],"円です")
      return fares[n]
    elif destination==99:
      print("駅の選択をキャンセルしました。")
      return 0
    else:
      print("数字を入力してください。")


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
