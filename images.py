import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('Ghandi.jpeg','Mohandas Karamchand Ghandi'),
       ('Zuckerberg.jpeg','Mark Zuckerberg'),
       ('Elizabeth.jpeg','Queen Elizabeth'),
       ('Swift.jpeg','Taylor Swift'),
       ('Agarwal.jpeg','Vednat Agarwal')
      ]
# Iterate through list to upload objects to S3   
for image in images:
   file = open(image[0],'rb')
   object = s3.Object('vedant-pictures',image[0])
   ret = object.put(Body=file,
                   Metadata={'FullName':image[1]}
                   )
   #print(image[0])
   #print(image[1])

