import { Component, ViewEncapsulation } from '@angular/core';
import { ExampleService } from './example.service';

@Component({
    selector     : 'example',
    templateUrl  : './example.component.html',
    encapsulation: ViewEncapsulation.None
})
export class ExampleComponent
{
    /**
     * Constructor
     */
    constructor(
        private _exampleService:ExampleService)
    {
    }
    // -----------------------------------------------------------------------------------------------------
    // @ Lifecycle hooks
    // -----------------------------------------------------------------------------------------------------

    /**
     * On init
     */
    ngOnInit(): void
    {
        // Create the form
       debugger
       this._exampleService.sstest().subscribe(
)
    }
}
