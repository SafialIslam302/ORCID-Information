# ORCID-Information

## Install Libraries
<b> pip install -r requirements.txt </b>

If any additional libraries are needed to install install it using <b> pip install (library name) </b>

## Input
Write all the ORCID id (Example: 0000-0002-0970-0455) in the <b> input_file.txt </b>. Write one orcid id per line. 

## Output
Make sure that you create a <b> Result </b> folder in the same directory. Otherwise it shows error. 
All the output files will save in the Result folder with the orcid id. Example: 0000-0002-0970-0455.txt

## Program run
All the code are written in restfull.py. In run.py import this file and use all the functions. 

First use the get function to find out which orcid id we need to find the information.
Example : ```orcid_res = restfull.get('0000-0002-0970-0455')```

Now if you want to extract information like family name write
```print(orcid_res.family_name)```

But for education, employment and publication orcid_res.educations, orcid_res.employments, and orcid_res.publications do not get the proper output. 
For those cases use any loop to extarct the information one by one. 
It will give the output in a JSON format. After getting the JSON format extract the exact information as you want. 
Example: 
* If you want to extarct any orcid id's publication title then write the following
```print(orcid_res.publications[0].title)```

* If you want to extarct any orcid id's employment department name then write the following
```orcid_res.employments[0]['department-name']```

* If you want to extarct any orcid id's educational organization name then write the following
```orcid_res.educations[0]['organization']['name']```

<b> If you want to extract more information into orcid id then add those attributes in the restfull.py file. </b>
This link will help you: https://github.com/ORCID/orcid-model/blob/master/src/main/resources/record_3.0/README.md

