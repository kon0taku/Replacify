# Replacify
Used to help craft wordlists, Replacify takes permutations from your source list and adds new lines replacing all instances of your keyword in the target file.

## OPTIONS
```
[REQUIRED] -s - set the path to the source list
[REQUIRED] -t - set the path to the target list
[REQUIRED] -w - set the word to replace in the target list

[OPTIONAL] -o - set the output filename
```


## NOTES

*The keyword is case sensitive. If you have 'password' set as the keyword, 'PASSWORD' will not be effected.




## EXAMPLE
###### Keyword
```
password
```

###### Source List
```
Password
P@ssword
P@5$word
p@5$w0rd
```

###### Target List
```
helloWorld
justApassword
mypassword
password1234
!!password!!
 ```
  
###### Output
```
helloWorld
justApassword
mypassword
password1234
!!password!!
justAPassword
justAP@ssword
justAP@5$word
justAp@5$w0rd
myPassword
myP@ssword
myP@5$word
myp@5$w0rd
Password1234
P@ssword1234
P@5$word1234
p@5$w0rd1234
!!Password!!
!!P@ssword!!
!!P@5$word!!
!!p@5$w0rd!!
```
