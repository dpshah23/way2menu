import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import {AngularFireModule } from '@angular/fire/compat';
import { initializeApp, provideFirebaseApp } from '@angular/fire/app';
import { getAuth, provideAuth } from '@angular/fire/auth';
import { getFirestore, provideFirestore } from '@angular/fire/firestore';
@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    AngularFireModule,
    provideFirebaseApp(() => initializeApp({"projectId":"way2menu-e0407","appId":"1:542346807588:web:5b5348183394ef55894bb1","storageBucket":"way2menu-e0407.appspot.com","apiKey":"AIzaSyDokqa_V86tcOIJpJ1EgIXrgaSlSmP3tYE","authDomain":"way2menu-e0407.firebaseapp.com","messagingSenderId":"542346807588"})),
    provideAuth(() => getAuth()),
    provideFirestore(() => getFirestore())
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }