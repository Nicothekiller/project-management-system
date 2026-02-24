from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import override

from sqlalchemy.orm import Session

from app.repositories.memory import InMemoryProjectRepo, InMemoryTaskRepo
from app.repositories.postgres import PostgresProjectRepo, PostgresTaskRepo

from app.infra.db import SessionLocal


class RepoFactory(ABC):
    @abstractmethod
    def create_project_repo(self):
        raise NotImplementedError()

    @abstractmethod
    def create_task_repo(self):
        raise NotImplementedError()


class MemoryRepoFactory(RepoFactory):
    def __init__(self) -> None:
        super().__init__()
        self._project_repo: InMemoryProjectRepo = InMemoryProjectRepo()
        self._task_repo: InMemoryTaskRepo = InMemoryTaskRepo()

    @override
    def create_project_repo(self):
        return self._project_repo

    @override
    def create_task_repo(self):
        return self._task_repo


class PostgesRepoFactory(RepoFactory):
    def __init__(self) -> None:
        super().__init__()
        self._session: Session = SessionLocal()
        self._project_repo: PostgresProjectRepo = PostgresProjectRepo(self._session)
        self._task_repo: PostgresTaskRepo = PostgresTaskRepo(self._session)

    @override
    def create_project_repo(self):
        return self._project_repo

    @override
    def create_task_repo(self):
        return self._task_repo
