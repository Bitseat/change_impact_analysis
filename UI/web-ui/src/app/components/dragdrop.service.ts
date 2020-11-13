import { Injectable } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { HttpErrorResponse, HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})

export class DragdropService {

  constructor(private http: HttpClient) { }

  addFiles(images: File[]) {
   
    var formData = new FormData();
 

    images.forEach((item, i) => {
      formData.append('avatar', item);
    });

    return this.http.post('http://localhost:8000/api/create-user', formData, {
      reportProgress: true,
      observe: 'events',
    }).pipe(
      catchError(this.errorMgmt),
    );
  }

  errorMgmt(error: HttpErrorResponse) {
    let errorMessage = '';
    if (error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    console.log(errorMessage);
    return throwError(errorMessage);
  }

}
