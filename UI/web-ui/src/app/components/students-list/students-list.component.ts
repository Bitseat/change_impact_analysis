import { Student } from './../../shared/student';
import { ApiService } from './../../shared/api.service';
import { Component, ViewChild, OnInit } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-students-list',
  templateUrl: './students-list.component.html',
  styleUrls: ['./students-list.component.css']
})

export class StudentsListComponent implements OnInit {
  StudentData: any = [];
  dataSource: MatTableDataSource<Student>;
  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  displayedColumns: string[] = ['issueid', 'similarity', 'description'];

  constructor(private studentApi: ApiService) {
    this.studentApi.GetStudents().subscribe(data => {
      this.StudentData = data;
      this.dataSource = new MatTableDataSource<Student>(this.StudentData);
      setTimeout(() => {
        this.dataSource.paginator = this.paginator;
      }, 0);
    })    
  }

  ngOnInit() { }

  

}