const payrollDashboardSection = document.getElementById('payroll-dashboard-section');
const payrollManagementSection = document.getElementById('payroll-management-section');
const employeeManagementSection = document.getElementById('employee-management-section');

const togglePayrollDashboard = document.getElementById('toggle-payroll-dashboard');
const togglePayrollManagement = document.getElementById('toggle-payroll-management');
const toggleEmployeeManagement = document.getElementById('toggle-employee-management');

const navPayroll = document.getElementById('nav-payroll');
const navEmployee = document.getElementById('nav-employee');
const navSettings = document.getElementById('nav-settings');

const hamburgerBtn = document.getElementById('hamburgerToggle');
const sidebar = document.querySelector('.sidebar');

const headerEl = document.querySelector('.header-title h1');

const switchView = (view) => {
    document.querySelectorAll('.view-toggle-bar button, .nav-item').forEach(btn => {
        btn.classList.remove('active');
    });

    payrollDashboardSection.classList.remove('active');
    payrollManagementSection.classList.remove('active');
    employeeManagementSection.classList.remove('active');

    if (view === 'dashboard') {
        payrollDashboardSection.classList.add('active');
        togglePayrollDashboard.classList.add('active');
        navPayroll.classList.add('active');
        document.querySelector('.breadcrumb').innerHTML = '<i class="fas fa-home"></i> Dashboard / Payroll';
        if (headerEl) headerEl.textContent = 'Company Payroll System';
    } else if (view === 'payroll') {
        payrollManagementSection.classList.add('active');
        togglePayrollManagement.classList.add('active');
        navPayroll.classList.add('active');
        document.querySelector('.breadcrumb').innerHTML = '<i class="fas fa-home"></i> Dashboard / Payroll Management';
        if (headerEl) {
            headerEl.textContent = 'Payroll Management';
            delete headerEl.dataset.fullTitle;
        }
    } else if (view === 'employee') {
        employeeManagementSection.classList.add('active');
        toggleEmployeeManagement.classList.add('active');
        navEmployee.classList.add('active');
        document.querySelector('.breadcrumb').innerHTML = '<i class="fas fa-home"></i> Dashboard / Employee Management';
        if (headerEl) {
            headerEl.textContent = 'Employee Management';
            delete headerEl.dataset.fullTitle;
        }
    }
};

togglePayrollDashboard.addEventListener('click', () => {
    switchView('dashboard');
});

togglePayrollManagement.addEventListener('click', () => {
    switchView('payroll');
});

toggleEmployeeManagement.addEventListener('click', () => {
    switchView('employee');
});

navPayroll.addEventListener('click', () => {
    switchView('dashboard');
});

navEmployee.addEventListener('click', () => {
    switchView('employee');
});

navSettings.addEventListener('click', () => {
    alert('Settings page coming soon');
});

if (hamburgerBtn && sidebar) {
    hamburgerBtn.addEventListener('click', () => {
        sidebar.classList.toggle('collapsed');
    });
}

switchView('dashboard');