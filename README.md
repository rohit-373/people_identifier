# people_identifier

**Problem Statement:**

- Nowadays in many offices, when new candidates gets employed, their faces are checked several times.

- First they check if the faces in hall ticket is same as in college identity card. If the faces match, they continue, else they are kept aside.

- Then, during interview, screenshots are being taken, to check if that candidate's face matches with the hall ticket.

- Once their faces matches everything, they get verified.

- However, this job is done by a staff in an office and imagine the staff verifying 100 of candidates.:face_with_head_bandage:

- To avoid so much stress, I made a small python code that verifies if the candidates faces matches:
  1. hall ticket and college identity
  2. hall ticket and screenshots in interview

**Requirements:**

- miniconda (get it from [here](https://docs.conda.io/en/latest/miniconda.html))

**Steps:**

1. Install miniconda

   ![image-20210304110336729](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304110336729.png)

2. While installing it, tick the option that says __Add Miniconda3 to my PATH environment variable__

3. After installation, go to the place with directories of different people

   ![image-20210304110830431](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304110830431.png)

4. Place all the codes there

   ![image-20210304111122489](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304111122489.png)

5. Make sure that the details of each candidate is in the directory `details`

   ![image-20210304111245552](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304111245552.png)

6. Inside directory of each candidate, make sure these PDF files exist:
   - `college_id.pdf` (college id of the candidate)
   - `hall_ticket.pdf` (hall ticket of the candidate)
   - `interview.pdf` (screenshots of the interview)

7.  Now once everything is verified, go back to the place where the codes exist

   ![image-20210304111825770](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304111825770.png)

8. Type `cmd` from there

9. Hit enter and the command prompt will open

   ![image-20210304112057914](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304112057914.png)

10. Type `conda activate base` and hit enter. It will activate miniconda.

    ![image-20210304112502681](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304112502681.png)

11. Type `conda create --name pi --file requirements.txt` as above

    ![image-20210304112720837](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304112720837.png)

12. Type `y` as above

    ![image-20210304112903206](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304112903206.png)

13. If it ends like this, then we can continue. If it ended up with an error then you have to start from first :(

14. After everything is done, type `conda activate pi` like below

    ![image-20210304114023480](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304114023480.png)

15. Once activated, type `pip install opencv-python` as below

    ![image-20210304114304640](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304114304640.png)

16. After installation, we are good to run the code :)

    ![image-20210304114541509](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304114541509.png)

17. Type `python candidate_verifier.py` and hit enter. Wait for a minute. It will end up like the above if no error occurred.

    ![image-20210304114825809](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304114825809.png)

18. Click the `candidate.txt` to see the output.

    ![image-20210304115119120](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304115119120.png)

19. You can import it as a CSV in excel for a better view :)

**Troubleshooting:**

- Make sure you followed the steps correctly

- Make sure you installed opencv correctly (see step 15)

- Make sure that the 3 files is there in each candidate directory

- If **one** of the files also doesn't exist, it will throw up an error like the below:

  ![image-20210304120842344](C:\Users\rohit_1bs7apt\AppData\Roaming\Typora\typora-user-images\image-20210304120842344.png)