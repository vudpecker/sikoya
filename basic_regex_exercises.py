import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

"""
[]	A set of characters	                                                        "[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	                                "he..o"	
^	Starts with	                                                                "^hello"	
$	Ends with	                                                                "planet$"	
*	Zero or more occurrences	                                                "he.*o"	
+	One or more occurrences	                                                    "he.+o"	
?	Zero or one occurrences	                                                    "he.?o"	
{}	Exactly the specified number of occurrences	                                "he.{2}o"	
|	Either or	                                                                "falls|stays"
"""