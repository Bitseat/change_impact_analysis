import { Router } from '@angular/router';
import { Component, OnInit, ViewChild, NgZone } from '@angular/core';
import { COMMA, ENTER } from '@angular/cdk/keycodes';
import { MatChipInputEvent } from '@angular/material/chips';
import { ApiService } from '../../shared/api.service';
import { FormGroup, FormBuilder, Validators, FormArray, FormControl } from "@angular/forms";

import { DragdropService } from "../dragdrop.service";
// import { FileUploadService } from "./file-upload.service";
import { HttpEvent, HttpEventType } from '@angular/common/http';
import { DomSanitizer } from '@angular/platform-browser';

export interface Subject {
  name: string;
}

@Component({
  selector: 'app-add-student',
  templateUrl: './train-model.component.html',
  styleUrls: ['./train-model.component.css']
})

export class TrainModelComponent implements OnInit {
 
  value: number = 0;
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
  SectioinArray: any = ['Moyo', 'Connect +'];

  //upload
  fileArr = [];
  imgArr = [];
  fileObj = [];
  // uploadForm: FormGroup;
  msg: string;
  progress: number = 0;
  

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
    private studentApi: ApiService,


    private sanitizer: DomSanitizer,
    public dragdropService: DragdropService

  ) { }

  
  /* Reactive book form */
  submitBookForm() {
    

    this.studentForm = this.fb.group({
      
      section: ['', [Validators.required]],
      candidate_name: ['', [Validators.required]],
      candidate_email: []
      // ,
      // avatars: ['', [Validators.required]]
      ,
      
      requirements: this.fb.array([]) ,
      issueid: [],
      similarity: [],
      description: []
      
     
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
    
    this.studentApi.AddModel(this.studentForm.value).subscribe(res => {
      this.ngZone.run(() => this.router.navigateByUrl('/train-model'))
      console.log(this.studentForm.value)
      console.log(this.studentForm.value)
    });
    
  }

  gg(e){
    console.log(e)
  }
  upload(e) {
    console.log(e)
    const fileListAsArray = Array.from(e);
    fileListAsArray.forEach((item, i) => {
      const file = (e as HTMLInputElement);
      const url = URL.createObjectURL(file[i]);
      this.imgArr.push(url);
      this.fileArr.push({ item, url: url });
    })

    this.fileArr.forEach((item) => {
      this.fileObj.push(item.item)
    })

    // Set files form control
    this.studentForm.patchValue({
      avatar: this.fileObj
    })

//     this.studentForm.get('avatar').updateValueAndValidity()

    // Upload to server
    this.dragdropService.addFiles(this.fileObj)
      .subscribe((event: HttpEvent<any>) => {
        switch (event.type) {
          case HttpEventType.Sent:
            console.log('Request has been made!');
            break;
          case HttpEventType.ResponseHeader:
            console.log('Response header has been received!');
            break;
          case HttpEventType.UploadProgress:
            this.value = Math.round(event.loaded / event.total * 100);
            console.log(`Uploaded! ${this.value}%`);
            break;
          case HttpEventType.Response:
            console.log('File uploaded successfully!', event.body);
            setTimeout(() => {
              this.value = 0;
              this.fileArr = [];
              this.fileObj = [];
              this.msg = "File uploaded successfully!"
            }, 3000);
        }
      })
  }

  // Clean Url for showing image preview
  sanitize(url: string) {
    return this.sanitizer.bypassSecurityTrustUrl(url);
  }

}


