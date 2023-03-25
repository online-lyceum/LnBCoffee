echo "Enter project name:"
read name
echo $1
mv api_template $1
find ./ find -type f -name "*" -not -path "./rename.sh" -exec sed -i "s//$1/g" {} \;
