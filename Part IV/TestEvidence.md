# Note:
This file includes the test evidence (screenshots) of 
1. Mock AWS services for Unit Testing (capture of result).
2. The process of manually uploading images to S3 Bucket on Amazon.
3. The Python Script to upload the photos programmatically.
4. Test notify-resize-fail-function scenario.

# 1. Mock AWS services for Unit Testing with some scenarios:
![Mock AWS Services for Unit Testing](<Screenshot_UnitTest/0. Mock AWS Services for Unit Testing.png>)

# 2. Test Evidence (Manually upload photos):
## A. Deployment:
**1. Before deploy, S3 is empty:**
![1. Before deploy, S3 is empty](<Screenshot_TestEvidence_ManuallyUpload/1. Before deploy, S3 is empty.png>)

**2. Before deploy, Lambda is empty:**
![2. Before deploy, Lambda is empty](<Screenshot_TestEvidence_ManuallyUpload/2. Before deploy, Lambda is empty.png>)

**3. Before deploy, CloudWatch is empty:**
![3. Before deploy, CloudWatch is empty](<Screenshot_TestEvidence_ManuallyUpload/3. Before deploy, CloudWatch is empty.png>)

**4. Before deploy, EventBus is empty:**
![4. Before deploy, EventBus is empty](<Screenshot_TestEvidence_ManuallyUpload/4. Before deploy, EventBus is empty.png>)

**5. Deployed, S3 buckets are created:**
![5. Deployed, S3 is created](<Screenshot_TestEvidence_ManuallyUpload/5. Deployed, S3 is created.png>)

**6. Deployed, restart-nikko-random-photos-upload bucket is empty:**
![6. Deployed, Upload Bucket is empty](<Screenshot_TestEvidence_ManuallyUpload/6. Deployed, Upload Bucket is empty.png>)

**7. Deployed, restart-nikko-random-photos-processed bucket is empty:**
![7. Deployed, Proccessed Bucket is empty](<Screenshot_TestEvidence_ManuallyUpload/7. Deployed, Proccessed Bucket is empty.png>)

**8. Deployed, Lambda functions are created:**
![8. Deployed, Lambda functions are created](<Screenshot_TestEvidence_ManuallyUpload/8. Deployed, Lambda functions are created.png>)

**9. Lambda process-image-function created:**
![9. Lambda process-image-function created](<Screenshot_TestEvidence_ManuallyUpload/9. Lambda process-image-function created.png>)

**10. Lambda notify-resize-success-function created:**
![10. Lambda notify-resize-success-function created](<Screenshot_TestEvidence_ManuallyUpload/10. Lambda notify-resize-success-function created.png>)

**11. Lambda notify-resize-fail-function created:**
![11. Lambda notify-resize-fail-function created](<Screenshot_TestEvidence_ManuallyUpload/11. Lambda notify-resize-fail-function created.png>)

**12. Deployed, CloudWatch Logs are created:**
![12. Deployed, CloudWatch is created](<Screenshot_TestEvidence_ManuallyUpload/12. Deployed, CloudWatch is created.png>)

**13. Deployed, EventBus image-processing-bus is created:**
![13. Deployed, EventBus is created](<Screenshot_TestEvidence_ManuallyUpload/13. Deployed, EventBus is created.png>)

## B. Test with image that has width LARGER THAN 200:
**14. Create uploads/ folder inside restart-nikko-random-photos-upload bucket, then upload image Manggo_700x368.jpg to uploads/ folder:**
![14. Uploads Folder_Manggo_700x368](<Screenshot_TestEvidence_ManuallyUpload/14. Uploads Folder_Manggo_700x368.png>)

**15. The image is resized and automatically uploaded to processed/ folder in restart-nikko-random-photos-processed bucket:**
![15. Processed Folder_Manggo_700x368 (Resized)](<Screenshot_TestEvidence_ManuallyUpload/15. Processed Folder_Manggo_700x368 (Resized).png>)

**16. Check CloudWatch Log of this process-image-function:**
![16. CloudWatch process-image-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/16. CloudWatch process-image-function Log (1).png>)

**17. CloudWatch Log: Original and Resized Image's Size (based on ratio):**
![17. CloudWatch process-image-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/17. CloudWatch process-image-function Log (2).png>)

**18. Check CloudWatch Log of notify-resize-success-function:**
![18. CloudWatch notify-resize-succcess-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/18. CloudWatch notify-resize-succcess-function Log (1).png>)

**19. CloudWatch Log: Status is "SUCCEEDED" and having Presigned URL of resized image:**
![19. CloudWatch notify-resize-succcess-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/19. CloudWatch notify-resize-succcess-function Log (2).png>)

**20. Copy and Paste Presigned URL on the Browser's Tab:**
![20. Test Presigned URL for Manggo_700x368](<Screenshot_TestEvidence_ManuallyUpload/20. Test Presigned URL for Manggo_700x368.png>)

## C. Test with image that has width EQUAL TO 200:
**21. Upload image Manggo_200x200.jpg to uploads/ folder:**
![21. Uploads Folder_Manggo_200x200](<Screenshot_TestEvidence_ManuallyUpload/21. Uploads Folder_Manggo_200x200.png>)

**22. The image is resized and automatically uploaded to processed/ folder in restart-nikko-random-photos-processed bucket:**
![22. Processed Folder_Manggo_200x200 (Resized)](<Screenshot_TestEvidence_ManuallyUpload/22. Processed Folder_Manggo_200x200 (Resized).png>)

**23. Check CloudWatch Log of this process-image-function:**
![23. CloudWatch process-image-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/23. CloudWatch process-image-function Log (1).png>)

**24. CloudWatch Log: Original and Resized Image's Size (based on ratio):**
![24. CloudWatch process-image-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/24. CloudWatch process-image-function Log (2).png>)

**25. Check CloudWatch Log of notify-resize-success-function:**
![25. CloudWatch notify-resize-succcess-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/25. CloudWatch notify-resize-succcess-function Log (1).png>)

**26. CloudWatch Log: Status is "SUCCEEDED" and having Presigned URL of resized image:**
![26. CloudWatch notify-resize-succcess-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/26. CloudWatch notify-resize-succcess-function Log (2).png>)

**27. Copy and Paste Presigned URL on the Browser's Tab:**
![27. Test Presigned URL for Manggo_200x200](<Screenshot_TestEvidence_ManuallyUpload/27. Test Presigned URL for Manggo_200x200.png>)

## D. Test with image that has width LESS THAN 200:
**28. Upload image Manggo_50x50.jpg to uploads/ folder:**
![28. Uploads Folder_Manggo_50x50](<Screenshot_TestEvidence_ManuallyUpload/28. Uploads Folder_Manggo_50x50.png>)

**29. The image is resized and automatically uploaded to processed/ folder in restart-nikko-random-photos-processed bucket:**
![29. Processed Folder_Manggo_50x50](<Screenshot_TestEvidence_ManuallyUpload/29. Processed Folder_Manggo_50x50.png>)

**30. Check CloudWatch Log of this process-image-function:** 
![30. CloudWatch process-image-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/30. CloudWatch process-image-function Log (1).png>)

**31. CloudWatch Log: Original and Resized Image's Size:**
(However, the width of this image is 50, which is less than 200. The Resized Image and Original Image have the same size)
![31. CloudWatch process-image-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/31. CloudWatch process-image-function Log (2).png>)

**32. Check CloudWatch Log of notify-resize-success-function:**
![32. CloudWatch notify-resize-succcess-function Log (1)](<Screenshot_TestEvidence_ManuallyUpload/32. CloudWatch notify-resize-succcess-function Log (1).png>)

**33. CloudWatch Log: Status is "SUCCEEDED" and having Presigned URL of resized image:**
![33. CloudWatch notify-resize-succcess-function Log (2)](<Screenshot_TestEvidence_ManuallyUpload/33. CloudWatch notify-resize-succcess-function Log (2).png>)

**34. Copy and Paste Presigned URL on the Browser's Tab:**
![34. Test Presigned URL for Manggo_50x50](<Screenshot_TestEvidence_ManuallyUpload/34. Test Presigned URL for Manggo_50x50.png>)

## E. After a period of time, those Presigned URLs above are expired and access is denied:
**35. Refresh the tab that has Presigned URL of the resized image of Manggo_700x368.jpg:**
![35. Test Presigned URL for Manggo_700x368 (Expired)](<Screenshot_TestEvidence_ManuallyUpload/35. Test Presigned URL for Manggo_700x368 (Expired).png>)

**36. Refresh the tab that has Presigned URL of the resized image of Manggo_200x200.jpg:**
![36. Test Presigned URL for Manggo_200x200 (Expired)](<Screenshot_TestEvidence_ManuallyUpload/36. Test Presigned URL for Manggo_200x200 (Expired).png>)

**37. Refresh the tab that has Presigned URL of the resized image of Manggo_50x50.jpg:**
![37. Test Presigned URL for Manggo_50x50 (Expired)](<Screenshot_TestEvidence_ManuallyUpload/37. Test Presigned URL for Manggo_50x50 (Expired).png>)


# 3. Test Evidence (Running Script to upload photos programmatically):
**1. Before running the Python Script to upload photos programmatically, the uploads/ folder in restart-nikko-random-photos-upload bucket is empty:**
![1. Script, Uploads Folder is empty](<Screenshot_TestEvidence_ScriptToUpload/1. Script, Uploads Folder is empty.png>)

**2. Before running the Python Script to upload photos programmatically, the processed/ folder in restart-nikko-random-photos-processed bucket is empty:**
![2. Script, Processed Folder is empty](<Screenshot_TestEvidence_ScriptToUpload/2. Script, Processed Folder is empty.png>)

**3. Running the script to programmatically upload two images into the uploads/ folder:**
![3. Run Script - 2 Photos added to Uploads Folder](<Screenshot_TestEvidence_ScriptToUpload/3. Run Script - 2 Photos added to Uploads Folder.png>)

**4. Two images are resized and automatically uploaded to processed/ folder in restart-nikko-random-photos-processed bucket:**
![4. Run Script - 2 Photos resized to Processed Folder](<Screenshot_TestEvidence_ScriptToUpload/4. Run Script - 2 Photos resized to Processed Folder.png>)

**5. Check CloudWatch Log of this process-image-function:**
![5. Run Script - CloudWatch process-image-function Log (1)](<Screenshot_TestEvidence_ScriptToUpload/5. Run Script - CloudWatch process-image-function Log (1).png>)

**6. CloudWatch Log: Original and Resized Image's Size of Manggo_700x368 (Red  Marking):**
![6. Run Script - CloudWatch process-image-function Log (2)](<Screenshot_TestEvidence_ScriptToUpload/6. Run Script - CloudWatch process-image-function Log (2).png>)

**7. CloudWatch Log: Original and Resized Image's Size of Manggo_700x700 (Blue  Marking):**
![7. Run Script - CloudWatch process-image-function Log (3)](<Screenshot_TestEvidence_ScriptToUpload/7. Run Script - CloudWatch process-image-function Log (3).png>)

**8. Check CloudWatch Log of notify-resize-success-function:**
![8. Run Script - CloudWatch notify-resize-successful-function Log (1).png](<Screenshot_TestEvidence_ScriptToUpload/8. Run Script - CloudWatch notify-resize-successful-function Log (1).png>)

**9. CloudWatch Log: Status of both image uploads are "SUCCEEDED" and having Presigned URLs of resized images:**
![9. Run Script - CloudWatch Log (2)](<Screenshot_TestEvidence_ScriptToUpload/9. Run Script - CloudWatch Log (2).png>)

**10. Copy and Paste Presigned URL of Manggo_700x700 (resized image) on the Browser's Tab:**
![10. Test Presigned URL for Manggo_700x700](<Screenshot_TestEvidence_ScriptToUpload/10. Test Presigned URL for Manggo_700x700.png>)

**11. CloudWatch Log: Status of both image uploads are "SUCCEEDED" and having Presigned URLs of resized images:**
![11. Run Script - CloudWatch Log (3)](<Screenshot_TestEvidence_ScriptToUpload/11. Run Script - CloudWatch Log (3).png>)

**12. Copy and Paste Presigned URL of Manggo_700x368 (resized image) on the Browser's Tab:**
![12. Test Presigned URL for Manggo_700x368](<Screenshot_TestEvidence_ScriptToUpload/12. Test Presigned URL for Manggo_700x368.png>)

**13. After a period of time, refresh the tab that has Presigned URL of the resized image of Manggo_700x700.jpg. The access is now denied:**
![13. Test Presigned URL for Manggo_700x700 (Expired)](<Screenshot_TestEvidence_ScriptToUpload/13. Test Presigned URL for Manggo_700x700 (Expired).png>)

**14. After a period of time, refresh the tab that has Presigned URL of the resized image of Manggo_700x368.jpg. The access is now denied:**
![14. Test Presigned URL for Manggo_700x368 (Expired)](<Screenshot_TestEvidence_ScriptToUpload/14. Test Presigned URL for Manggo_700x368 (Expired).png>)

# 4. Test notify-resize-fail-function scenario:
**1. To test the failed scenario, I changed a line of correct code by commenting out on AWS and deployed again:**
![1. Test the fail scenario by changing a line of correct code](<Screenshot_Test_notify_resize_fail_function/1. Test the fail scenario by changing a line of correct code.png>)

**2. Upload image Manggo_700x700.jpg to uploads/ folder:**
![2. Uploads Folder_Manggo_700x700](<Screenshot_Test_notify_resize_fail_function/2. Uploads Folder_Manggo_700x700.png>)

**3. Check processed/ folder then and nothing is there:**
![3. Processed Folder is empty](<Screenshot_Test_notify_resize_fail_function/3. Processed Folder is empty.png>)

**4. Check CloudWatch Log of this process-image-function:**
![4. CloudWatch process-image-function Log (1)](<Screenshot_Test_notify_resize_fail_function/4. CloudWatch process-image-function Log (1).png>)

**5. CloudWatch Log of process-image-function shows there are errors:**
![5. CloudWatch process-image-function Log (2)](<Screenshot_Test_notify_resize_fail_function/5. CloudWatch process-image-function Log (2).png>)

**6. Check CloudWatch Log of notify-resize-success-function and there is no new log:**
![6. CloudWatch notify-resize-success-function Log (1)](<Screenshot_Test_notify_resize_fail_function/6. CloudWatch notify-resize-success-function Log (1).png>)

**7. Check CloudWatch Log of notify-resize-fail-function:**
![7. CloudWatch notify-resize-fail-function Log (1)](<Screenshot_Test_notify_resize_fail_function/7. CloudWatch notify-resize-fail-function Log (1).png>)

**8.CloudWatch Log: Status is "FAILED" printed:**
![8. CloudWatch notify-resize-fail-function Log (2)](<Screenshot_Test_notify_resize_fail_function/8. CloudWatch notify-resize-fail-function Log (2).png>)


