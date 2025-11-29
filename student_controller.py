from flask import Blueprint, render_template, request, redirect, url_for
from models.student_model import *

student_bp = Blueprint("students", __name__, url_prefix="/students")


@student_bp.route("/")
def list_students():
    students = get_all_students()
    return render_template("students.html", students=students)


@student_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        add_student(request.form["name"], request.form["email"])
        return redirect(url_for("students.list_students"))
    return render_template("add_student.html")


@student_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    student = get_student(id)

    if request.method == "POST":
        update_student(id, request.form["name"], request.form["email"])
        return redirect(url_for("students.list_students"))

    return render_template("edit_student.html", student=student)


@student_bp.route("/delete/<int:id>")
def delete(id):
    delete_student(id)
    return redirect(url_for("students.list_students"))
