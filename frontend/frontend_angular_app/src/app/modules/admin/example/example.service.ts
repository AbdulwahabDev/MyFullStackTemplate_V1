import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { of, switchMap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ExampleService {

  constructor(
    private _httpClient: HttpClient
    ) { }


    sstest()
    {
      debugger
      return this._httpClient.get('http://127.0.0.1:3101/users/get_verified_current_user_or_none',{}).pipe(
                switchMap((response: any) => {
     
              
                    return of(response);
                })
            );
    }
}


