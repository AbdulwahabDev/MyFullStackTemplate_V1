import { ChangeDetectionStrategy, Component, ViewEncapsulation } from '@angular/core';

@Component({
    selector       : 'chat-empty-conversation',
    templateUrl    : './empty-conversation.component.html',
    encapsulation  : ViewEncapsulation.None,
    changeDetection: ChangeDetectionStrategy.OnPush
})
export class EmptyConversationComponent
{
    /**
     * Constructor
     */
    constructor()
    {
    }
}
