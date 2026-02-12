from datetime import date
from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infra.db import Base


class ProjectModel(Base):
    __tablename__: str = "projects"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    tasks: Mapped[list["TaskModel"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class TaskModel(Base):
    __tablename__: str = "tasks"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    project_id: Mapped[str] = mapped_column(
        String, ForeignKey("projects.id"), nullable=False
    )

    title: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    due_date: Mapped[Date | None] = mapped_column(Date, nullable=True)

    task_type: Mapped[str] = mapped_column(String, nullable=False)

    project: Mapped["ProjectModel"] = relationship(back_populates="task")
