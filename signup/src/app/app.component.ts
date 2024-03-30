import { Component } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
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
  constructor(private dataService: DataService) { }
  ngOnInit(): void {}

  send(){
    this.dataService.send(this.name,this.logo,this.address,this.owner_name,this.gst_number,this.owner_age,this.owner_gender,this.owner_number,this.owner_email,this.account_password).subscribe((result: any)=>
    (console.warn(result)))
  }
}
