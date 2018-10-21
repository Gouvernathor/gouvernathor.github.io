#/bin/sh

python3 _build/generate_config.py > _config.yml

for l in $(cat _build/languages.csv | cut -d";" -f1)
do
	mkdir -p _$l
	
	echo "---" > _$l/index.html
	echo "layout: index" >> _$l/index.html
	echo "permalink: /"$l"/" >> _$l/index.html
	echo "language: "$l >> _$l/index.html
	echo "---" >> _$l/index.html
	
	echo "---" > _$l/help.html
	echo "layout: help" >> _$l/help.html
	echo "language: "$l >> _$l/help.html
	echo "---" >> _$l/help.html
	
	echo "---" > _$l/quiz.html
	echo "layout: quiz" >> _$l/quiz.html
	echo "language: "$l >> _$l/quiz.html
	echo "---" >> _$l/quiz.html
	
	echo "---" > _$l/results.html
	echo "layout: results" >> _$l/results.html
	echo "language: "$l >> _$l/results.html
	echo "---" >> _$l/results.html
done
