import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private API_URL = 'http://localhost:8000/api'; // Replace with your Python server URL

  constructor(private http: HttpClient){}

  sendPrompt(data: any): Observable<any> {

    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const requestOptions = {
      headers: headers,
      responseType: 'text' as 'json', // For text streams, use 'text'. For binary data, you might use 'blob' or 'arraybuffer'.
      observe: 'body' as 'body'
    };
    return this.http.post(`${this.API_URL}/prompt`, {"prompt": data}, requestOptions);

    //return dummy value
   /*  return new Observable<any>(observer => {
      //observer.next({ message: 'This is a dummy response' });
      observer.next('This is a dummy response');
      observer.complete();
    }); */
  }
}
