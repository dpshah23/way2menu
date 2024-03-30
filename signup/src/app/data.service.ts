import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http: any;

  constructor() { }
  send(name:any,logo:any,address:any,owner_name:any,gst_number:any,owner_age:any,owner_gender:any,owner_number:any,owner_email:any,account_password:any){
    const data={name:name,logo:logo,address:address,owner_name:owner_name,gst_number:gst_number,owner_age:owner_age,owner_gender:owner_gender,owner_number:owner_number,owner_email:owner_email,account_password:account_password};
    return this.http.post('http://127.0.0.1:8000/addrestaurant/',data);
  }
}