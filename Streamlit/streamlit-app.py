import streamlit as st
import pandas as pd

st.header("Basic Streamlit application")

global employees 
global department

try:
    employees = pd.read_csv('employees.csv')
    department = pd.read_csv('department.csv')
except FileNotFoundError:
    employees = pd.DataFrame(index='empno', columns=['empno', 'ename','job', 'deptno'])
    department = pd.DataFrame(index='deptno', columns=['deptno', 'dname', 'loc'])

def employees_page():
    global employees
    st.title("Employee")
    emp_no = st.text_input("Add Employee Number")
    emp_name = st.text_input("Add Employee Name")
    job = st.text_input("Job")
    dept_no = st.text_input("Department Number")
    if st.button("Add Employee"):
        emp_dict = {'empno': [emp_no], 'ename': [emp_name], 'job': [job], 'deptno': [dept_no]}
        employees = pd.concat([employees, pd.DataFrame(emp_dict)], ignore_index=True)
        st.success("EMPLOYEE ADDED!")
        visualization()

def department_page():
    global department
    st.title("Department")
    st.write(department)
    dept_no = st.text_input("Add Department Number")
    dept_name = st.text_input("Add Department Name")
    location = st.text_input("Location")
    if st.button("Add Department"):
        dept_dict = {'deptno':[dept_no], 'dname':[dept_name], 'loc':[location]}
        department = pd.concat([department, pd.DataFrame(dept_dict)], ignore_index=True)
        st.success("DEPARTMENT ADDED!")
        visualization()


def visualization():
    st.title("Employees")
    st.write(employees)
    st.title("Department")
    st.write(department)

def join():
    st.write(employees.merge(department, on='deptno', how='inner'))

def main():
    st.sidebar.title('App Switcher')

    page = st.sidebar.radio("Select a page:", ("Visualization", "Employees", "Department"))

    if page == "Employees":
        employees_page()
    elif page == "Department":
        department_page()
    else:
        visualization()

    if st.button("JOIN TWO TABLES"):
        join()

    employees.to_csv('employees.csv', index=False)
    department.to_csv('department.csv', index=False)


if __name__ == '__main__':
    main()
