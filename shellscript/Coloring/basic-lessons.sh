# Shellscript - Comments for Human. Computer will ignore that line. It will execute it

echo "Hello Ayush"

read -p "Enter the Color name" picked_color

echo "You entered Color : $picked_color " 

#[1,2,3,4]

colors=(red green yellow orange brown blue)

for colorName in "${colors[@]}"
do

  mkdir -p colors/${colorName[@]}
  echo  "I am ${colorName[@]}"  > colors/${colorName[@]}/open_me.txt
  echo "${colorName[@]}"

done



