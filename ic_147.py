def menu():
  #ここに処理の中身を書く()カッコ内の引数はある場合は書く。
  functions =["乗車駅選択", "チャージ機能"]

  print("【ウチダ電鉄 交通系 IC カード検証システム】")
  
  for i in range(len(functions)):
    print(str(i+1) +": "+functions[i])

  while True:
    try: 
      n=int(input("使用する機能を入力してください（終了する場合には99 を入力）")) 
    except ValueError: #int("abcd")とか入力されたときに数値に変換できないから　
      print("正しい数値を入力してください。")
    else:#エラーが起きなかった場合
      if 1<= n <= len(functions) or n==99 : #1以上でfunctionsというリストの長さ以下の　nの値しか　合格しない
        return n 
      else:
        print("正しい数値を入力してください。")


  

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


def pay(balance,fare):
  print(f"チャージ残高は{balance}円です。")
  if balance < fare:
    print("残高不足です")
    while True:
      if balance < fare:
        print("3000円自動でチャージします")
        balance=balance + 3000
      else:
        break

  balance = balance - fare
  print(f"清算後のチャージ残高は{balance}円です。")
  if balance < 500:
    balance = balance + 3000
    print("チャージ残高が500円未満なので3000円自動でチャージします")
  return balance

  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。


def charge(balance): #引数はbalaneにした　英語の　残高
  charges=[] 
  for i in range(1000,10001,1000): #1000から10000まで１０００ずつすすむ
    charges.append(i)

  print("【チャージ機能】")
  print(f"チャージ残高は{balance}円です。")
  for i in range(len(charges)):
      print(f"{i+1}: {charges[i]}円") #今回はcharges[i]もint型のため

  while True:
    try:
      n = int(input("チャージする金額を選択してください。（キャンセルする場合には99を入力"))
    except ValueError: #1.5とかabcdとか入力されたときに
      print("正しい数値を入力してください。")
    else: #エラー起きなかったら
      if 1<= n <= len(charges) or n==99:
        break
      else:
        print("正しい数値を入力してください。")

  if  1<= n <= len(charges):
    print(f"{charges[n-1]}円チャージします") #nが１のとき　1000でcharges[0]の値だから　n-1するとちょうど
    balance=balance+charges[n-1]#残高についかしておく
  elif n==99:
    print("チャージをキャンセルしました。")  
  print(f"チャージ残高は{balance}円です。")
  return balance
  
  


def main():
  #ここに処理の中身を書く。()カッコ内の引数はある場合は書く。
  pass #このpassは処理を書いた後消してよい。
  m = menu()
  if m == 1:
    print("まだ実装できてない")
  elif m ==2:
    charge(500)    
  print(m)
  
 

if __name__ == "__main__":
    main() 
