import { Route } from '@angular/router';
import { ChatChatResolver, ChatChatsResolver, ChatContactsResolver, ChatProfileResolver } from 'app/modules/admin/apps/chat/chat.resolvers';
import { ChatComponent } from 'app/modules/admin/apps/chat/chat.component';
import { ChatsComponent } from 'app/modules/admin/apps/chat/chats/chats.component';
import { ConversationComponent } from 'app/modules/admin/apps/chat/conversation/conversation.component';
import { EmptyConversationComponent } from 'app/modules/admin/apps/chat/empty-conversation/empty-conversation.component';

export const chatRoutes: Route[] = [
    {
        path     : '',
        component: ChatComponent,
        resolve  : {
            chats   : ChatChatsResolver,
            contacts: ChatContactsResolver,
            profile : ChatProfileResolver
        },
        children : [
            {
                path     : '',
                component: ChatsComponent,
                children : [
                    {
                        path     : '',
                        pathMatch: 'full',
                        component: EmptyConversationComponent
                    },
                    {
                        path     : ':id',
                        component: ConversationComponent,
                        resolve  : {
                            conversation: ChatChatResolver
                        }
                    }
                ]
            }
        ]
    }
];
