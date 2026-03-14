<h1 align="center">Loan Approval Prediction Using Multiple Machine Learning Models</h1>

<p align="center">
This project predicts whether a loan application will be approved or rejected using multiple machine learning algorithms.
It helps financial institutions automate loan approval decisions based on applicant financial information.
</p>

<hr>

<h2>🔗 Project Links</h2>

<ul>
<li><b>GitHub Repository:</b> 
<a href="https://github.com/GanjiNagendhraPrasad/Loan-Approval-Prediction-Using-Multiple-Machine-Learning-Models.git">
View Source Code</a></li>

<li><b>Live Demo:</b> 
<a href="https://loan-approval-prediction-using-multiple.onrender.com/">
Open Web Application</a></li>
</ul>

<hr>

<h2>📌 Project Overview</h2>

<p>
The <b>Loan Approval Prediction</b> project is a machine learning system designed to determine whether a loan application should be approved or rejected.
Banks receive thousands of loan applications every day, and manually verifying them can be time-consuming and prone to human error.
</p>

<p>
This project uses historical applicant data and applies multiple machine learning models to predict loan approval outcomes automatically.
The goal is to help financial institutions make faster, data-driven decisions.
</p>

<hr>

<h2>🎯 Problem Statement</h2>

<p>
Financial institutions must evaluate whether an applicant is eligible for a loan.
The traditional manual verification process is slow and inefficient.
</p>

<p>The objective of this project is to build a a machine learning model that can classify loan applications into:</p>

<ul>
<li>Approved</li>
<li>Rejected</li>
</ul>

<hr>

<h2>📊 Dataset Description</h2>

<table border="1" cellpadding="8">
<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Dependents</td>
<td>Number of dependents supported by the applicant</td>
</tr>

<tr>
<td>Education</td>
<td>Graduate or Not Graduate</td>
</tr>

<tr>
<td>Self Employed</td>
<td>Whether the applicant is self-employed</td>
</tr>

<tr>
<td>Income</td>
<td>Annual income of the applicant</td>
</tr>

<tr>
<td>Loan Amount</td>
<td>Requested loan amount</td>
</tr>

<tr>
<td>Loan Term</td>
<td>Duration of the loan</td>
</tr>

<tr>
<td>CIBIL Score</td>
<td>Credit score representing financial reliability</td>
</tr>

<tr>
<td>Residential Assets</td>
<td>Value of residential properties</td>
</tr>

<tr>
<td>Commercial Assets</td>
<td>Value of commercial properties</td>
</tr>

<tr>
<td>Luxury Assets</td>
<td>Value of luxury items owned</td>
</tr>

<tr>
<td>Bank Asset Value</td>
<td>Total bank asset value</td>
</tr>

<tr>
<td>Loan Status</td>
<td>Target variable indicating approval or rejection</td>
</tr>

</table>

<hr>

<h2>⚙️ Project Workflow</h2>

<h3>1. Data Collection</h3>
<p>The dataset contains both numerical and categorical variables related to loan applicants.</p>

<h3>2. Data Preprocessing</h3>

<ul>
<li><b>Handling Missing Values</b> – Cleaning or replacing missing data.</li>
<li><b>Encoding Categorical Variables</b> – Converting text features into numerical values.</li>
<li><b>Outlier Detection</b> – Identifying abnormal values.</li>
<li><b>Feature Scaling</b> – Normalizing numerical features.</li>
</ul>

<hr>

<h2>🤖 Machine Learning Models Used</h2>

<h3>1. Logistic Regression</h3>
<ul>
<li>Simple and interpretable classification algorithm</li>
<li>Predicts probability of loan approval</li>
</ul>

<h3>2. Decision Tree</h3>
<ul>
<li>Tree-based model that splits data using feature conditions</li>
<li>Easy to visualize and interpret</li>
</ul>

<h3>3. Random Forest</h3>
<ul>
<li>Ensemble method using multiple decision trees</li>
<li>Improves prediction accuracy and reduces overfitting</li>
</ul>

<h3>4. Gradient Boosting</h3>
<ul>
<li>Sequential learning algorithm</li>
<li>Corrects errors made by previous models</li>
</ul>

<h3>5. XGBoost</h3>
<ul>
<li>Highly optimized gradient boosting algorithm</li>
<li>Widely used in machine learning competitions</li>
</ul>

<h3>6. Neural Network (MLPClassifier)</h3>
<ul>
<li>Multi-layer neural network for learning complex patterns</li>
</ul>

<hr>

<h2>📈 Model Training</h2>

<ul>
<li>Training Data – 80%</li>
<li>Testing Data – 20%</li>
</ul>

<hr>

<h2>📊 Model Evaluation</h2>

<ul>
<li>Accuracy</li>
<li>Precision</li>
<li>Recall</li>
<li>F1 Score</li>
<li>Confusion Matrix</li>
</ul>

<hr>

<h2>🏆 Results</h2>

<ul>
<li>Random Forest and XGBoost performed better than basic models.</li>
<li>Credit score strongly influences loan approval.</li>
<li>Income and assets affect eligibility.</li>
</ul>

<hr>

<h2>💻 Technologies Used</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Scikit-learn</li>
<li>Matplotlib</li>
<li>Seaborn</li>
</ul>

<hr>

<h2>🚀 Applications</h2>

<ul>
<li>Banks</li>
<li>Financial Institutions</li>
<li>Credit Companies</li>
<li>Online Loan Platforms</li>
</ul>

<hr>

<h2>📌 Conclusion</h2>

<p>
This project demonstrates how machine learning can automate the loan approval process.
By comparing multiple algorithms, the system identifies the most effective model for predicting loan eligibility.
</p>

<p align="center">
⭐ If you like this project, consider giving it a star on GitHub!
</p>
