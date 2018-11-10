eosiocpp -o Simplememo.wast Simplememo.cpp 
eosiocpp -g Simplememo.abi Simplememo.cpp 
cleos -u http://jungle.cryptolions.io:18888/ set contract daidaides121 ../Simplememo/ -p daidaides121@active
cleos -u http://jungle.cryptolions.io:18888/ push action daidaides121 addmemo ["hoge1","hoge2"] -p daidaides121@active
cleos -u http://jungle.cryptolions.io:18888/ get table daidaides121 daidaides121 memo
