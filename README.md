# ****SOF output file analysis****

General information about the files in the `SOFDATA` folder:

### Consider the following data (located in the specified folder):
```bash
    1- The `Answer` table, which includes the following information from the answers published on `SOF`:
```

* **Answer number** .<br>
* **Date of the answer** .<br>
* **Number of votes for the answer** .<br>
* **Responder's ID** .<br>
* **Number of comments** .<br>
* **Closure date (only not null if the answer has been closed)** .<br>

```bash
    2- The 'Question' table, which contains the following information from the questions published on 'SOF':
```
* **Question number** .<br>
* **Date of the question** .<br>
* **Number of votes for the question** .<br>
* **Number of times the question was viewed** .<br>
* **Asker's ID** .<br>
* **Number of comments** .<br>
* **Closure date (only not null if the question has been closed)** .<br>
* **Number of times the question was marked as 'Favorite'** .<br>

```bash
    3- The 'Q-A' table, which includes the following information from the questions and answers published on 'SOF':
```
* **Question number** .<br>
* **Answer number** .<br>
* **Is the answer marked as 'Accepted'** .<br>

```bash
    4- The 'U' table includes the following information from active individuals on 'SOF' (askers or responders):
```
* **Person's ID** .<br>
* **Person's 'Reputation'** .<br>
* **Number of times the person's page was viewed** .<br>
* **Number of 'UPvotes'** .<br>
* **Number of 'Downvotes'** .<br>

```bash
    5- The 'user-badge' table, which contains the following information about individuals:
```
*  **Person's ID** .<br>
*  **Name of the 'badge' received by the person"** .<br>
<br>


## ***Using data visualization, you accept or reject the following hypotheses:***

**1**- Questions with an `Accepted` answer receive more `Views`.
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q1/README.md)/)


**2**- Questions with more `Views` receive more `Comments`.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q2/README.md)/)

**3**- An answer receives more likes if the related question has many likes.<br>

[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q3/README.md)/)


**4**- Individuals with high `Reputation` tend to respond to questions that receive many likes.<br>

[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q4/README.md)/)


**5**- Individuals with high `Reputation` tend to respond to closed questions.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q5/README.md)/)

**6**- Individuals with a higher number of `Badges` have higher `Reputation`.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q6/README.md)/)

**7**- The shorter the time delay in responding (the less time between the question and the answer), the higher the chance of the answer being accepted.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q7/README.md)/)

**8**- If we categorize questions into four groups: unanswered, with few answers, with a moderate number of answers, and with many answers, the likelihood of getting likes increases from right to left.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q8/README.md)/)

**9**- The number of `Views` a question receives correlates with the number of likes it gets.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q9/README.md)/)

**10**- If individuals are divided into three categories of `Low-Medium-High Reputation`, the   questions from individuals with `High Reputation` receive more likes.<br>
[Go to Answar]([https://github.com](https://github.com/Hadikamali/SOF-output-file-analysis-part-two/tree/main/Answer-Q10/README.md)/)

----------

