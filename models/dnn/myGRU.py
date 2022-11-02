import torch




def gru1_forward(input,sent_lens,h0,w_ih,w_hh,b_ih,b_hh,w_ih0,w_hh0,b_ih0,b_hh0):#可以进行去零操作
        '''
            input:[seq_len,batch_size,d_rnn_in]   58  54  300
            h0:  [batch_size,d_rnn_in] ---54,300  用于存储上一时间步的状态

            w_ih:900,300
            w_hh:900,300
            b_ih:900
            b_hh:900

            w_ih0:900,300
            w_hh0:900,300
            b_ih0:900
            b_hh0:900
        '''
        
        input_lens=sent_lens
        prev_h = h0#[batch_size,d_rnn_in]
        bs,T,i_size = input.shape  #[seq_len,batch_size,d_rnn_in]   58  54  300    
        h_size = w_ih.shape[0]//3   #300 gru中隐含神经元的个数
        #对权重扩维，复制成batch_size倍
        # batch_w_ih = w_ih.unsqueeze(0).repeat(bs,1,1)#[seq_len,900,d_h1]                
        # batch_w_hh = w_hh.unsqueeze(0).repeat(bs,1,1)
        output = torch.zeros(bs,T,i_size)   #[seq_len,batch_size,d_rnn_in(d_h1)]
        for t in range(T): #对每个batch进行取值                                            
            #x= input[:,t,:]  #X: seq_len,d_rnn_in  
            #print(input[:,t,:],input[:,t,:].shape) 
            x= input[0:input_lens[t],t,:]                                                   #----------5.7改，进行对0的切分                                                  
            #print(x,x.shape)   
            #对权重扩维，复制成batch_size倍
            batch_w_ih = w_ih.unsqueeze(0).repeat(bs,1,1)[0:input_lens[t],:,:]#[seq_len,900,d_h1]                
            batch_w_hh = w_hh.unsqueeze(0).repeat(bs,1,1)[0:input_lens[t],:,:]

            w_times_x = torch.bmm(batch_w_ih,x.unsqueeze(-1)) #矩阵批量相乘
            w_times_x = w_times_x.squeeze(-1) #[seq_len,900] 
            prev_h=h0[0:input_lens[t],:]
            w_times_h_prev = torch.bmm(batch_w_hh,prev_h.unsqueeze(-1))###################
            w_times_h_prev = w_times_h_prev.squeeze(-1)#[seq_len,900]
                                                                                                                                                                             
            a = w_times_x[:,:h_size].data#[batch_size,300]
            b =w_times_h_prev[:,:h_size].data#[batch_size,300]
            c =b_ih[:h_size].view(1,300).data#(1,300)
            d =b_hh[:h_size].view(1,300).data#(1,300)
            r_t=torch.cat((a,b,c,d),dim=0)#进行拼接 size：(118,300)-----58*2+1*2
            r_t=torch.max(r_t,dim=0)[0]

            r_t = torch.sigmoid(r_t)#将结果映射到0-1之间
            w_x = w_times_x[:,h_size:2*h_size].data
            w_h = w_times_h_prev[:,h_size:2*h_size].data
            b_i = b_ih[h_size:2*h_size].view(1,300).data
            b_h = b_hh[h_size:2*h_size].view(1,300).data
            z_t = torch.cat((w_x,w_h,b_i,b_h),dim=0)
            z_t=torch.max(z_t,dim=0)[0]
            z_t=torch.sigmoid(z_t)
           
            w_times = w_times_x[:,2*h_size:3*h_size].data
            b_ihh =b_ih[2*h_size:3*h_size].view(1,300).data
            r_tt = r_t*(w_times_h_prev[:,2*h_size:3*h_size]+b_hh[2*h_size:3*h_size]).data
            n_t = torch.cat((w_times,b_ihh,r_tt),dim=0)
            n_t =torch.max(n_t,dim=0)[0]
            n_t = torch.tanh(n_t)
            prev_h1 = (1-z_t)*n_t +z_t*prev_h.data#[batch,300]  这就是当前记忆内容
            #对当前内容进行填充                                                 ----5.7加
            com_tensor=torch.tensor(np.zeros((bs-prev_h1.shape[0],prev_h1.shape[1]))).to(torch.float32).cuda()
            prev_h1=torch.cat((prev_h1,com_tensor),dim=0)
            output[:,t,:] = prev_h1#对output进行填充
                  
        h_size0 = w_ih0.shape[0]//3 #300
        # batch_w_ih0 = w_ih0.unsqueeze(0).repeat(bs,1,1)
        # batch_w_hh0 = w_hh0.unsqueeze(0).repeat(bs,1,1)
       
        output0 = torch.zeros(bs,T,i_size)
        for t in range(T-1,-1,-1):
            x= input[0:input_lens[t],t,:] 
            batch_w_ih0 = w_ih0.unsqueeze(0).repeat(bs,1,1)[0:input_lens[t],:,:]#[seq_len,900,d_h1]                
            batch_w_hh0 = w_hh0.unsqueeze(0).repeat(bs,1,1)[0:input_lens[t],:,:]

            w_times_x0 = torch.bmm(batch_w_ih0,x.unsqueeze(-1))
            w_times_x0 = w_times_x0.squeeze(-1)
            prev_h=h0[0:input_lens[t],:]
            w_times_h_prev0 = torch.bmm(batch_w_hh0,prev_h.unsqueeze(-1))
            w_times_h_prev0 = w_times_h_prev0.squeeze(-1) 

            a0 = w_times_x0[:,:h_size0].data #h_size0
            b0 =w_times_h_prev0[:,:h_size0].data
            c0 =b_ih0[:h_size0].view(1,300).data
            d0 =b_hh0[:h_size0].view(1,300).data
            r_t0 = torch.cat((a0,b0,c0,d0),dim=0)
            r_t0 =torch.max(r_t0,dim=0)[0]
            r_t0 = torch.sigmoid(r_t0)

            w_x0 = w_times_x0[:,h_size0:2*h_size0].data#h_size0
            w_h0 = w_times_h_prev0[:,h_size0:2*h_size0].data
            b_i0 = b_ih0[h_size0:2*h_size0].view(1,300).data
            b_h0 = b_hh0[h_size0:2*h_size0].view(1,300).data
            z_t0 = torch.cat((w_x0,w_h0,b_i0,b_h0),dim=0)
            z_t0 =torch.max(z_t0,dim=0)[0]
            z_t0 = torch.sigmoid(z_t0)

            w_times0 = w_times_x0[:,2*h_size0:3*h_size0].data
            b_ihh0 =b_ih0[2*h_size0:3*h_size0].view(1,300).data
            r_tt0 = r_t0*(w_times_h_prev0[:,2*h_size0:3*h_size0]+b_hh0[2*h_size0:3*h_size0]).data
            n_t0 = torch.cat((w_times0,b_ihh0,r_tt0),dim=0)
            n_t0 =torch.max(n_t0,dim=0)[0]
            n_t0 = torch.tanh(n_t0)
            prev_h0 = (1-z_t0)*n_t0 +z_t0*prev_h.data
            #对当前内容进行填充                                                 ----5.7加
            com_tensor1=torch.tensor(np.zeros((bs-prev_h0.shape[0],prev_h0.shape[1]))).to(torch.float32).cuda()
            prev_h0=torch.cat((prev_h0,com_tensor1),dim=0)
            #prev_h=prev_h0                                                                  #m加，5.6更新隐藏状态权重
            output0[:,t,:] = prev_h0

        output_out = torch.cat([output0, output], dim=-1)#按列拼接 size:[batch_size,seq_len,2*d_rnn_in],   prev_h[batch,d_rnn_in]
        return output_out,prev_h