#!/bin/bash

# Static analysis
flake8 .

RESULT=$?
if [ ${RESULT} != "0" ]; then
	echo -e "\nOh no, looks like you have some issues, please correct them.
If you want to ignore an specific issue, code '# noqa' in the related line.
To more information, visit: http://flake8.pycqa.org/en/latest/index.html\n"
	exit ${RESULT}
fi

echo -e "\nGreat, no issues here to report.\n"

exit 0
