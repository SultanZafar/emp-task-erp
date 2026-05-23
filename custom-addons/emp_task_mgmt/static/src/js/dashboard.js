/** @odoo-module **/
import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class ETMDashboard extends Component {
    static template = "emp_task_mgmt.Dashboard";

    setup() {
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = useState({
            employees: [],
            total_employees: 0,
            in_progress: 0,
            done_tasks: 0,
            unpaid: 0,
        });
        onWillStart(async () => {
            await this.loadData();
        });
    }

    async loadData() {
        const emps = await this.orm.searchRead("hr.employee.custom", [], ["name", "department", "status"]);
        this.state.employees = emps;
        this.state.total_employees = emps.length;
        const tasks = await this.orm.searchRead("emp.task", [], ["name", "status"]);
        this.state.in_progress = tasks.filter(t => t.status === "in_progress").length;
        this.state.done_tasks = tasks.filter(t => t.status === "done").length;
        const payrolls = await this.orm.searchRead("emp.payroll", [], ["status"]);
        this.state.unpaid = payrolls.filter(p => p.status === "unpaid").length;
    }

    openEmployee(empId) {
        const self = this;
        return function() {
            self.action.doAction({
                type: "ir.actions.act_window",
                res_model: "hr.employee.custom",
                res_id: empId,
                views: [[false, "form"]],
                target: "current",
            });
        };
    }

    openEmployeeList() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "hr.employee.custom",
            views: [[false, "list"], [false, "form"]],
            target: "current",
        });
    }

    openInProgress() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "emp.task",
            views: [[false, "list"], [false, "form"]],
            domain: [["status", "=", "in_progress"]],
            target: "current",
        });
    }

    openDone() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "emp.task",
            views: [[false, "list"], [false, "form"]],
            domain: [["status", "=", "done"]],
            target: "current",
        });
    }

    openPayrollList() {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: "emp.payroll",
            views: [[false, "list"], [false, "form"]],
            domain: [["status", "=", "unpaid"]],
            target: "current",
        });
    }
}

registry.category("actions").add("etm_dashboard", ETMDashboard);