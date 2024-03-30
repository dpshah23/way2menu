import { Component } from '@angular/core';

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
  owner_address=null;
}
