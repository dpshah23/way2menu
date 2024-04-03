import { Component } from '@angular/core';
import { DataService } from './data.service';
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  title = 'signup';
  name='';
  logo:File|null=null;
  address='';
  owner_name='';
  gst_number=null;
  owner_age=null;
  owner_gender=null;
  owner_number=null;
  owner_email=null;
  account_password=null;
  range=null;
  active=false;
  constructor(private dataService: DataService) { }
  ngOnInit(): void {}
image(): void{
  const file=this.logo;
  if(file){
    console.log(file);
  }
}
  send(){
    this.dataService.send(this.name,this.address,this.owner_name,this.gst_number,this.owner_age,this.owner_gender,this.owner_number,this.owner_email,this.account_password,this.range,this.active).subscribe((result: any)=>
    (console.warn(result)))
  }
}
