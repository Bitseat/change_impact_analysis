import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddStudentComponent } from './components/add-student/add-student.component';
import { StudentsListComponent } from './components/students-list/students-list.component';
import { TrainModelComponent } from './components/train-model/train-model.component';
import { HelpComponent } from './components/Help/help.component';
// import { ViewerComponent } from './components//viewer.component';
import { ReqTestComponent } from './components/req-test/req-test.component';


const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'add-student' },
  { path: 'add-student', component: AddStudentComponent },
  { path: 'students-list', component: StudentsListComponent },
  { path: 'train-model', component: TrainModelComponent },
  { path: 'check-id', component: AddStudentComponent },
  { path: 'req-test', component: ReqTestComponent },
  { path: 'help', component: HelpComponent }
 
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }