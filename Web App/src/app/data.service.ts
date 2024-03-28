import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  send(email:any,password:any){
    const data={email:email,password:password};
    return this.http.post('http://127.0.0.1:8000/login/',data);
  }
}
