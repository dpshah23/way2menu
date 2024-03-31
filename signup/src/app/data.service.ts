import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http: any;

  constructor() { }
  send(name:any,active:any,address:any,owner_name:any,gst_number:any,owner_age:any,owner_gender:any,owner_number:any,owner_email:any,account_password:any,range:any){
    const data={restaurant_name:name,address:address,owner_name:owner_name,gstno:gst_number,owner_age:owner_age,owner_gender:owner_gender,mobile:owner_number,email:owner_email,password:account_password,range:range,active:active};
    return this.http.post('http://127.0.0.1:8000/addrestaurant/',data);
  }
}