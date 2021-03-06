import { Router } from '@angular/router';
import { Component, OnInit, ViewChild, NgZone } from '@angular/core';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import { ApiService } from '../../shared/api.service';
import { FormGroup, FormBuilder, Validators, FormArray, FormControl } from "@angular/forms";

export interface Subject {
  name: string;
}

@Component({
  selector: 'app-req-test',
  templateUrl: './req-test.component.html',
  styleUrls: ['./req-test.component.css']
})

export class ReqTestComponent implements OnInit {
  name = 'Angular';
  productForm: FormGroup;

  visible = true;
  selectable = true;
  removable = true;
  addOnBlur = true;
  @ViewChild('chipList', { static: true }) chipList;
  @ViewChild('resetStudentForm', { static: true }) myNgForm;
  readonly separatorKeysCodes: number[] = [ENTER, COMMA];
  studentForm: FormGroup;
  subjectArray: Subject[] = [];
  SectioinArray: any = ['A', 'B', 'C', 'D', 'E'];
  
  ngOnInit() {
    this.submitBookForm();
    this.productForm = this.fb.group({

      name: '',

      quantities: this.fb.array([]) ,

    });
  }

  constructor(
    public fb: FormBuilder,
    private router: Router,
    private ngZone: NgZone,
    private studentApi: ApiService
  ) { }

  
  /* Reactive book form */
  submitBookForm() {
    this.studentForm = this.fb.group({
      candidate_name: ['', [Validators.required]],
      candidate_email: ['', [Validators.required]]
     
     
    })
  }

  /* Add dynamic languages */
  add(event: MatChipInputEvent): void {
    const input = event.input;
    const value = event.value;
    // Add language
    if ((value || '').trim() && this.subjectArray.length < 5) {
      this.subjectArray.push({ name: value.trim() })
    }
    // Reset the input value
    if (input) {
      input.value = '';
    }
  }

  /* Remove dynamic languages */
  remove(subject: Subject): void {
    const index = this.subjectArray.indexOf(subject);
    if (index >= 0) {
      this.subjectArray.splice(index, 1);
    }
  }  

  /* Date */
  formatDate(e) {
    var convertDate = new Date(e.target.value).toISOString().substring(0, 10);
    this.studentForm.get('dob').setValue(convertDate, {
      onlyself: true
    })
  }  

  /* Get errors */
  public handleError = (controlName: string, errorName: string) => {
    return this.studentForm.controls[controlName].hasError(errorName);
  }  

  /* Submit book */
  submitStudentForm() {
    if (this.studentForm.valid) {
      this.studentApi.TestReq(this.studentForm.value).subscribe(res => {
        this.ngZone.run(() => this.router.navigateByUrl('/req-test'))
      });
      
    }
  } 

}


