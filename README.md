# auto-stop-ec2
Lambda + CloudWatchでEC2の自動起動停止をするオートメーションです。

#起動停止のルール
処理の起動・停止のルールです。

・毎日EC2を9時に起動する。
・毎日EC2を21時に停止する。
・ただし、土日・祝日は処理をスキップする。

土日・祝日の入力は手動で行う必要がありますが、起動・停止は自動で行います。


