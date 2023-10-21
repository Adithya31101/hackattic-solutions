for n in {1000..999999};
do
  unzip -P $n -o package.zip secret.txt
  EXIT_CODE=$?
  echo $EXIT_CODE
  if [$EXIT_CODE -eq 0 ];then
    echo "Password Found $n"
    break
  fi
  if [$EXIT_CODE -eq 2 ];then
    rm secret.txt
    break
  fi
done