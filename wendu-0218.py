# /home/pi/wendu-0218.py

#########################################################　
# 温度値を取得                          	        	#
#########################################################
#OpenFile
tfile = open("/sys/bus/w1/devices/28-00000494cb79/w1_slave")
#data Read
text = tfile.read()
#CloseFile
tfile.close()
#データ変換
secondline = text.split("\n")[0]
#スペースでデータを分割し、配列を生成、t を取得
wendudata = secondline.split(" ")[20]
wendu = float(wendudata[2:])
#温度値に変換
wendu= wendu / 1000

#########################################################
# yeelink：中国有名なIoTデータPF（無料）。			#
# yeelinkのアカウント申請・設備とセンサーの追加は割愛		#
# yeelink API規則により、JSON形式のtxtファイルが必要：	#
# {							#
# “timestamp”:”2012-03-15T16:13:14″,			#
# “value”:294.34					#
# }							#
# Timestampは今回不要。なければサーバ側自動追加。		#
#########################################################
# Yeelinkへ転送のため、データを加工(JSONフォーマット)
# JSONフォーマットに書く
res = '{"value":%f}' %wendu
# JSONを/home/pi/wendudata.txtに書き込む
output = open('/home/pi/wendudata.txt', 'w')
output.write(res)
output.close
res = '{"value":%f}'%wendu
output = open('/home/pi/wendudata.txt','w')
output.write(res)
output.close()
